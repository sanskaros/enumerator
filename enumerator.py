from os import system
print(" __")
print("|--  _       _  _   _   _  _  -|-  _   _                    ")
print("(__ / | |_| / |/ ) |-' /  |_|  |  |_| /    V0.0.1           ")
print("                    ``       `             -Stat_of_mind    ")
Enumerate=input("Enter the target url(format:example.com): ")
system("curl -s 'https://crt.sh/?q={}' | grep '<TD>' | grep {} | cut -d '>' -f2 | cut -d '<' -f1 | sort -u | sed '/^*/d' | tee -a {}.txt".format(Enumerate,Enumerate,Enumerate))
system("curl -s 'https://rapiddns.io/subdomain/{}#result' | grep '<td><a' | cut -d '\"' -f 2 | grep http | cut -d '/' -f3 | sed '/^*/d' | tee -a {}.txt".format(Enumerate,Enumerate))
system("curl -s 'https://jldc.me/anubis/subdomains/{}' | grep -Po '((http|https):\/\/)?(([\w.-])\.([\w])\.([A-z]))\w+' | cut -d '/' -f3 | sort -u | tee -a {}.txt".format(Enumerate,Enumerate))
system("sort {}.txt | uniq | sed '/^*/d' | tee -a {}".format(Enumerate,Enumerate))
system(f"rm -r {Enumerate}.txt")
system(f"cat {Enumerate} | httpx -o {Enumerate}")