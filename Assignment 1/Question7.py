org_str=input('Enter the String:')
patterns=input('Enter the pattern:')
if org_str.startswith(patterns) or org_str.endswith(patterns):
    print(f'{org_str} contains {patterns}')
else:
    print(f'{org_str} does not contain {patterns}')
        