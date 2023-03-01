import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const kue = require('kue');
const queue = kue.createQueue();

describe('createPushNotificationsJobs', function () {
	before(function () {
		queue.testMode.enter();
	});

	afterEach(function () {
		queue.testMode.clear();
	});

	after(function () {
		queue.testMode.exit();
	});

	it ('display a error message if jobs is not an array', function () {
		expect(function() {
			createPushNotificationsJobs({ foo: 'bar' }, queue)
		}).to.throw(Error,'Jobs is not an array');

	});

	it ('checkes if the jobs are created', function () {
		createPushNotificationsJobs([{
			phoneNumber: '4153518780',
			message: 'This is the code 1234 to verify your account'
		  }], queue);

		expect(queue.testMode.jobs.length).to.equal(1);
		expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
		expect(queue.testMode.jobs[0].data).to.eql({
			phoneNumber: '4153518780',
			message: 'This is the code 1234 to verify your account'
		  });
	})
})
