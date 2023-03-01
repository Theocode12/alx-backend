const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message);
	done();
})

// process.once( 'SIGTERM', function ( sig ) {
// 	queue.shutdown( 5000, function(err) {
// 	  console.log( 'Kue shutdown: ', err||'' );
// 	  process.exit( 0 );
// 	});
// });
