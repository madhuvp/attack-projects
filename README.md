# Cert-Chain-Check

This program checks the validity of certificate chains and verifies the authenticity of the intermediate chains, establishing no-trust policy except the root. 

The algorithm works as follows. :
1.	We initialize the store variable to an X509 object 
2.	We get the root “TRUSTED_CERTS_PEM” in this program, with the certify.where() command.
3.	We are allowed to trust the root, so we parse the root with pem.parse() command and add it to another variable, which is stored using the store.add_cert() command.
4.	Then, we get all the intermediate nodes, from get_cert_chain() function, including the target domain and store it in a variable called, say “chain”
5.	Now chain is reversed, because the verification should happen from the last.
6.	Each certificate is checked and verified, if it is, it gets added to the store variable and we return “True”
7.	Otherwise, we return “False”
