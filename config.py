import sys

def config(arg):
    global DISABLE_EMAIL_SENDING
    global GET_EXAMPLE_FORMS
    global DISABLE_FREEZING
    global INTERNAL_TESTING

    # Default setting
    DISABLE_EMAIL_SENDING = True
    GET_EXAMPLE_FORMS = True
    DISABLE_FREEZING = True
    INTERNAL_TESTING = False

    length = len(arg)
    for position in range(1,length):
        # Set modes
        if arg[position] == "--release_mode":
            print("Running in release mode!")
            DISABLE_EMAIL_SENDING = False
            GET_EXAMPLE_FORMS = False
            DISABLE_FREEZING = False
            INTERNAL_TESTING = False
            return
        elif arg[position] == "--internal_testing_mode":
            print("Running in internal testing mode!")
            print("Files will be extracted from testing files!")
            DISABLE_EMAIL_SENDING = True
            GET_EXAMPLE_FORMS = False
            DISABLE_FREEZING = False
            INTERNAL_TESTING = True
            return
        # Set parameters
        elif arg[position] == "--disable_email_sending":
            print("Disable email")
            DISABLE_EMAIL_SENDING = True
        elif arg[position] == "--disable_freezing":
            print("Disable freezing")
            DISABLE_FREEZING = True
        elif arg[position] == "--use_example":
            print("Use example")
            GET_EXAMPLE_FORMS = True

        # If not on the list
        else:
            raise ValueError('Invalid command line option', arg[position])
    return


if __name__ == "__main__":
    config(sys.argv)