#%% This was my first attempt: 11%/11%. Relatively poor performance.
#class Solution:
#    def interpret(self, command: str) -> str:
#        output = ""
#        while command:
#            if command[0] == 'G':
#                output += 'G'
#                command = command[1: len(command)]
#            elif command[0: 2] == '()':
#                output += 'o'
#                command = command[2: len(command)]
#            elif command[0:4] == '(al)':
#                output += 'al'
#                command = command[2: len(command)]
#            else: command = command[1: len(command)]
#        return output
    
#%% Here's another approach with better performance.
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')