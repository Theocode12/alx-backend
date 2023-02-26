import { createClient, print } from 'redis';
const util = require('util');

const client = createClient();
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))

client.on('connect', () => console.log('Redis client connected to the server'));

const get = util.promisify(client.get)
const set = util.promisify(client.set)

async function setNewSchool(schoolName, value) {
	const result = await set(schoolName, value)
	console.log(result)
}

async function displaySchoolValue(schoolName) {
	const value = await get(schoolName)
	console.log(value);
}

async function main() {
	client.on('connect', async () => {
		console.log(client.connected)
		await displaySchoolValue('Holberton');
		await setNewSchool('HolbertonSanFrancisco', '100');
		await displaySchoolValue('HolbertonSanFrancisco');
	});
}

main();
