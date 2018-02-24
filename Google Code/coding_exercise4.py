# def search_for(needle, haystack):
# def search_for(needle: str, haystack: str):
def search_for(needle: str, haystack: str) -> int:
	offset = haystack.find(needle)
	return offset


print(search_for('bc', 'abcdefghij'))
#print(search_for(123, 'abcdefghij'))