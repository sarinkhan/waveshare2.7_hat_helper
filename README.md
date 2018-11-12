# waveshare2.7_hat_helper
The goal of this is to provide some helper functions for the waveshare ePaper display in python on a raspberry pi.
It is based on the waveshare epaper display library <a href="https://gist.github.com/sarinkhan/3500a4495308295ce7f8ef8e9fc0769d">gist to help install it</a>.

It adds some functions that enable easier use of the display, without the need to make so many calculation.

For now, it is a quick and dirty project, based on the main.py example from the waveshare library. I'll tidy it up later,
and turn it into a proper project.

For now it will just provide a few methods to draw things, with an example use case : a clock.
