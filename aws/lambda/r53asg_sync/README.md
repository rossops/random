Purpose:

The purpose of this is to update R53 "A" records when a scale event happens so that
the record has the most up to date information on the instances it points to. This 
acts as a Lambda endpoint for ASG events (scale up/down) that get sent through SNS.