function createPushNotificationsJobs(jobs, queue) {
	if (Array.isArray(jobs)) {
		for(let job of jobs) {
			const cJob = queue.create('push_notification_code_3',
				job).save((err) => {
					if (!err) {
						console.log(`Notification job created: ${cJob}`)
					}
			});
      cJob.on('complete', (result) => {
        console.log(`Notification job ${cJob.id} completed`);
      }).on('failed', (error) => {
        console.log(`Notification job ${cJob.id} failed: ${error}`);
      }).on('progress', (progress, data) => {
        console.log(`Notification job ${cJob.id} ${progress}% complete`)
      });
		}
	} else {
	  throw (new Error('Jobs is not an array'));
  }
}

module.exports = createPushNotificationsJobs;
