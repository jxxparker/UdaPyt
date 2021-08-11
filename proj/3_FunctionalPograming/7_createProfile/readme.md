In this exercise, you'll write a function named create_profile. This function should require at least one positional argument (someone's given name, and a variadic collection of surnames or modifiers) and must handle a variadic collection of keyword-specified arguments with details from a profile.

You'll need to define the function signature so that it can be called in the following valid ways:

create_profile('Sam')
create_profile('Sam', role='Instructor')
create_profile('Martin', 'Luther', 'King', 'Jr', born=1929, died=1968)
create_profile("Sebastian", "Thrun", cofounded="Udacity", experience="Stanford Professor")

It must be invalid to call this function as create_profile() with no arguments.

In each of the valid cases, you should print out something like the following:

create_profile('Sam')
# Sam

create_profile('Sam', role='Instructor')
# Sam
# role: Instructor

create_profile('Martin', 'Luther', 'King', 'Jr', born=1929, died=1968)
# Martin Luther King Jr.
# born: 1929
# died: 1968

create_profile("Sebastian", "Thrun", cofounded="Udacity", experience="Stanford Professor")
# Sebastian Thrun
# cofounded: Udacity
# experience: Stanford Professor
As a first step, what should be the function's signature?