const redis = require('redis');
const util = require('util');
const express = require('express');
const app = express();

const client =  redis.createClient();
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))

client.on('connect', () => console.log('Redis client connected to the server'));

client.get = util.promisify(client.get);
client.set = util.promisify(client.set);

const listProducts = [
	{itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4},
	{itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10},
	{itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2},
	{itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5}
]

function getItemById(id) {
	return listProducts[id - 1];
}

function reserveStockById(itemId, stock) {
	const item = getItemById(itemId)
	if (item && item.initialAvailableQuantity > 0) {
		item.initialAvailableQuantity -= stock;
		client.set(itemId, JSON.stringify(item));
	}
}

async function getCurrentReservedStockById(itemId) {
	return await client.get(itemId)
}

app.use(express.json());

app.get('/list_products', (req, res) => {
	res.json(listProducts);
	res.end();
})

app.get('/list_products/:itemId', async (req, res) => {
	const fullStock = getItemById(req.params.itemId);
	const currentReseverdStock = JSON.parse(await getCurrentReservedStockById(req.params.itemId));
	if (fullStock && currentReseverdStock) {
		fullStock.currentQuantity = fullStock.initialAvailableQuantity - currentReseverdStock.initialAvailableQuantity
		res.json(fullStock);
		res.end();
	} else if (fullStock) {
		fullStock.currentQuantity = fullStock.initialAvailableQuantity
		res.json(fullStock);
		res.end();
	} else {
		res.status(404).json({ status: 'Product not found' })
		res.end();
	}
})

app.get('/reserve_product/:itemId', async (req, res) => {
	const fullStock = getItemById(req.params.itemId);
	let currentReseverdStock = JSON.parse(await getCurrentReservedStockById(req.params.itemId));
	if (fullStock && currentReseverdStock) {
		if ((fullStock.initialAvailableQuantity - currentReseverdStock.initialAvailableQuantity) > 0) {
			reserveStockById(fullStock.itemId, 1);
			res.json({"status":"Reservation confirmed","itemId":1});
			res.end();
		} else {
			res.json({"status":"Not enough stock available","itemId":`${req.params.itemId}`});
			res.end();
		}
		res.end()
	} else if (fullStock) {
		reserveStockById(fullStock.itemId, 1);
		res.json({"status":"Reservation confirmed","itemId":1});
		res.end();
	} else {
		res.status(404).json({"status":"Product not found"})
	}
})


app.listen(1245, () => console.log('listening on 1245'));
