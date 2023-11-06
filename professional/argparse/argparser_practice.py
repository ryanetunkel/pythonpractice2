import argparse

# Assigns parser to be an Argument Parser
parser = argparse.ArgumentParser()

# Echo
# Adds what cmd line options the program is willing to accept.
# Means calling the method requires you to specify an option
# help adds a descriptive message about the arg when you call --help

# parser.add_argument("echo", help="echo the string you use here")

# # Returns some data from the options specified

# args = parser.parse_args()
# print(args.echo)


# Square
# similar, but does the square of a num
# Won't work unless specify type is an int. Default is treating it as a string
# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)


# Optional Args
# Makes it so the program displays something when --verbosity is specified
# It displays nothing when --verbosity is not specified
# --verbosity is proven to be an optional arg as there is no error
# when the program runs without adding --verbosity (now --verbose)

# this new implementation makes it so the option is more of a flag than a value requirement
# action = "store_true" means that if the option is specified, assign the
# value True to args.verbose. Not specifying it implies False
# -v is the short option of it
# parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")


# Combining Positional and Optional arguments
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print(f"the square of {args.square} equals {answer}")
# else:
#     print(answer)

# Multiple Verbosity Values
# added choices so csn only do 0-2 for verbosity
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v","--verbosity", type=int,  choices=[0, 1, 2],
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)

# My own
# parser.add_argument("increment", type=int, 
#                     help="increment a given number by a number")
# parser.add_argument("amount", type=int, 
#                     help="increment a number by a given number")
# parser.add_argument("-t","--times", type=int,
#                     help="number of times to increment a number by a number")
# args = parser.parse_args()
# if args.times:    
#     answer = args.increment + (args.amount * args.times)
# else:
#     answer = args.increment + args.amount
# print(answer)

# The "count" action
# makes it so instead of 0,1,2 you can do -v, -vv, and -vvv (same as none)
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v","--verbosity", action="count",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)

# Updating so only -v and -vv do uniques and any v's more do the same as -vv
# Adds a default of 0 too - without the default tag it is "None"
# which isn't an int and therefore can't be compared in the ifs
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v","--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)

