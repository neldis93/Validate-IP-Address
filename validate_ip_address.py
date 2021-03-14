import re

def validateIpAddress(IP:str) -> str:
    IPv4Pattern = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$')
    IPv6Pattern = re.compile(r'^(([0-9a-fA-F]{1,4})\:){7}([0-9a-fA-F]{1,4})$')

    if IPv4Pattern.match(IP):
        return "IPv4"
    elif IPv6Pattern.match(IP):
        return "IPv6"
    else:
        return "IP incorrect"

if __name__ == '__main__':
    print(validateIpAddress("8.8.8.8"))


