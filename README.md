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

# circuit-list
A list of all Tor circuits my machine currently uses, as specified by the list of three Tor relays.
Output looks like “entry node–middle node–exit node.”

#Hash-Extension-Attack
Code that demonstrates a hash extension attack in SHA 256

Here, we try to elevate our privileges by adding ",admins" to the existing permissions. We extend the hash by padding the original text to be 8 byte short of 64 and then the length of the string for 8 bytes. Now, we append the malicious string we want to add. It takes the input, computes, and returns output in hexadecimal.

Then it uses the originally found hash as the base values and tries to compute a new hash with the new padding and the altered hash.

This would match the hash found in the malicious string if it had been added originally.
