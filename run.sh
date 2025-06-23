#!/bin/sh
# Simple script to test the project locally
set -x  # use this if failiures are okay and the script should continue
# set -x -e  # use this if the script should stop at failiures, e.g. failed tests

# Remove all hatch environments, which forces a re-creation of them in the next
# steps to ensure that they are correctly created
hatch env prune  # this can be commented out if only smaller changes have been made

# Run all the tests and provide a coverage report
hatch run test:cov

# Run all the tests again, this time taking into account all the specified pythons
# versions this project should be compatible to. This will take a while and can be
# commented out if not needed.
hatch run py-test:cov

# Lint the project
hatch run lint:all
# The above command is the same as running the two individual ones below
# hatch run lint:style
# hatch run lint:typing
# Additionally, if the linting reports the option of automatic fixes, the following
# command can be used to perform them
# hatch run lint:fix

# Build the package
hatch build

# Generate the documentation
hatch run docs:generate
hatch run docs:build

# Optional: Serve the documentation on a local webserver
# hatch run docs:serve
