list = ["Artifial Interligence", "My home"]
def shortForm(sentence):
    for  i in sentence:
        x=i.split()
        print(x)
        short_form=""
        for j in x:
            short_form=short_form + j[0]
        print(short_form.upper())


shortForm(list)