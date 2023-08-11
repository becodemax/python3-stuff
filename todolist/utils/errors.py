
class Errors:

    def getErrorCmd(err) -> str:
        match err:
            case "display_list":
                error = "\nShowing command failed: syntax error or [number] out of reach.\n"
            case "add_to_list":
                error = '\nAdding command failed: syntax error.\n'
            case "remove_from_list":
                error = '\nRemoving command failed: syntax error.\n'
            case "done":
                error = '\nThe "done" command failed: syntax error.\n'
            case "change":
                error = "\nChanging command failed: syntax error or [number] out of reach.\n"
            case "prompt":
                error = '\nUnknown command. Type "help" for more info.\n'
            case "exit":
                error = '\nPlease enter a valid option or leave blank.\n'
            case _:
                error = '\nSomething went wrong.\n'

        return error
    
    def getErrorFile(err, file) -> str:
        match err:
            case "open_file":
                error = f'\nError: File {file} not found.\n'
            case _:
                error = '\nSomething went wrong.\n'

        return error