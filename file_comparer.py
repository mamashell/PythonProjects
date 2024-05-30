from difflib import unified_diff

title = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
File Comparer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
  
with open('file_1.txt', 'r') as file_1, open('file_2.txt', 'r') as file_2: # ADJUST FILE NAMES HERE
    lines1 = file_1.readlines()
    lines2 = file_2.readlines()

    diff = list(unified_diff(lines1, lines2, fromfile='file_1.txt', tofile='file_2.txt')) # ADJUST FILE NAMES HERE

    additions = []
    deletions = []
    common_lines = []
    unknowns = []
    hunks = []

    for line in diff:
        if line.startswith('@@'):
            hunks.append(line)
        elif line.startswith('+') and not line.startswith('+++'):
            additions.append(line)
        elif line.startswith('-') and not line.startswith('---'):
            deletions.append(line)
        elif line.startswith(' '):
            common_lines.append(line)
        elif line.startswith('?'):
            unknowns.append(line)
            
  
    with open('differences.txt', 'w') as output_file:
        output_file.write(title + '\n')

        # Write headers for the diff sections
        output_file.write("File 1: --- file_1.txt\n") # ADJUST FILE NAME (OPTIONAL)
        output_file.write("File 2: +++ file_2.txt\n") # ADJUST FILE NAME (OPTIONAL)

        # Write the hunk headers
        if hunks:
            output_file.write("\n\nHunk Header (Lines Being Compared):\n")
        for hunk in hunks:
            output_file.write(hunk)
        
        # Write the changes as they appear in the diff
        if common_lines:
            output_file.write("\n\nCommon in Both Files:\n")
            for common in common_lines:
                output_file.write(common)
        
        # Write the deletions
        if deletions:
            output_file.write("\n\nUnique to File 1:\n")
            for deletion in deletions:
                output_file.write(deletion)
        
        # Write the additions
        if additions:
            output_file.write("\n\nUnique to File 2:\n")
            for addition in additions:
                output_file.write(addition)

        # Write the unknowns
        if unknowns:
            output_file.write("\n\nLine not Present in Either File:\n")
            for unknown in unknowns:
                output_file.write(unknown)
