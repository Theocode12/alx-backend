const redis = require('redis');
const util = require('util');
const kue = require('kue');
const express = require('express');

const app = express();
app.use(express.json());

const queue = kue.createQueue();

const client = redis.createClient()
let available_seats = 50;
let reservationEnabled = true;

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))
client.on('connect', () => console.log('Redis client connected to the server'));

client.get = util.promisify(client.get);
client.set = util.promisify(client.set);


function reserveSeat(number) {
	client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
	return await client.get('available_seats');
}

app.get('/available_seats', (req, res) => {
	res.json({"numberOfAvailableSeats": `${available_seats}`});
})

app.get('/reserve_seat', (req, res) => {
	if (reservationEnabled) {
		const job = queue.create('reserve_seat',
			{ "status": "Reservation in process" }).save((err) => {
				if (!err) {
					console.log(`Seat reservation job ${job.id} completed`)
					res.json({ "status": "Reservation in process" });
				} else {
					console.log(`Seat reservation job ${job.id} failed: ${err}`);
					res.json({ "status": "Reservation failed" })
				};
			})
	} else {
		res.json({ "status": "Reservation are blocked" });
	}
})

app.get('/process', async (req, res) => {
	queue.process('reserve_seat', (job, done) => {
		available_seats -= 1
		reserveSeat(available_seats);
		if (available_seats >= 0) {
			if (available_seats === 0) {
				reservationEnabled = false;
			}
		} else {
			done(new Error('Not enough seats available'))
		}
		done();
	})
	res.json({ "status": "Queue processing"})
})

app.listen(1245, () => console.log('listening on 1245'));
