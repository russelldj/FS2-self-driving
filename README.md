# Full-scale full-stack self driving
The idea of this work is to implement limited autonomy for a full-sized car on a few simplistic tasks with the hope of developing a robust experimentation platform. 

# Goal
The problem I would like to initially tackle is driving through a slalom course. The slalom gates would be marked with [AprilTags](https://april.eecs.umich.edu/software/apriltag) and the system would be responsible for steering the car, with a safety driver applying the gas

# TODOs
As I see it, this project can be broken into a set of somewhat-distinct tasks

### Perception
Given the image from a front-facing camera find the AprilTags and extract their location in the 2D space. This should be fairly easy as we can make the tags arbitrarily-large. Given that AprilTags are pretty robust and give orientation and a unique identifier they seem like the best choice, but it's possible there are better options out there that I don't know about.

### Planning
To make this work easily, there would likely need to be a hardcoded list which contains the ordering of the gates. As the vision system detects gates, the planner would need to chart a course to the next detected gate. This could probably be done with [Dubin's Paths](https://en.wikipedia.org/wiki/Dubins_path) but more sophisticated approaches like splines and bezier curves could be explored. This step would also require the creation of a decent visualizer. 

### Control
Given an path and the current location of the vehicle, the controler would need to output the correct steeting angle. Potentially acccelleration would be added in the future, but for now this is just done by the human. Note that this appraoch will need to be robust to the noise which is unavoidable in perception and actuation in a real-world setting. I'm not quite sure how this would be done, but it seems that there have to be common approaches. One simple idea would be to use a PID controler to itteratively progress toward landmarks sampled from the future of the trajectory, though this might be jerky


### Actuation
To make any of this work, the steering wheel needs to be actually turned. I have a few ideas for how to do this fall into the camps of attaching a belt to the wheel and driving it with a pully, or pressing a high-friction wheel or tread against the wheel. In either case, the motor could be mouned to the cowling on top of the dashboard.

### Power System
There will need to be a few components to power Jetson TX2 (the brains) and the actuation system, with the latter likely requiring far more power. I have a motor and some drivers which require 36VDC so potentially led-acid batteries would be enough. The Jetson should be run off 120VAC, though it might be possible to also run it directly with (properly-filtered) DC. It doesn't require much power though.

# Hardware
I have couple of things which I think should be pretty helpful:
* A Jetson TX2 developer kit with a built-in camera. This should be powerful enough to run everything in (near)realtime 
* 300 oz/in (big) stepper motors with associated power supplies and control boards
* An '08 Subie on the verge of death

This should be a lot of the high-cost parts, but there are a few things I envision us having to purchase:
* Batteries and converters to run the electronics
* The hardware to drive the wheel, likely belts, wheels, clamps and such


-----

Let's get this bread Yuhhhh!
