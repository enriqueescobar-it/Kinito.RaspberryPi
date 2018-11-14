import tkinter
import http.client
import json

root = tkinter.Tk()
#label =  tkinter.Label(root,text="Hello from TKinter")
#label.pack()
listbox = tkinter.Listbox(root)
text  = tkinter.Entry(root)

def buttonclick():
    c = http.client.HTTPConnection('search.twitter.com')
    c.request('GET','/search.json?q={0}'.format(text.get()))
    r = c.getresponse()
    data = r.read()
    datas = str(data,'utf-8')
    o = json.loads(datas)
    tweets = o['results']
    listbox.delete(0,tkinter.END)
    for tweet in tweets:
        listbox.insert(tkinter.END,tweet['text'])
        #print(tweet['text'])

button = tkinter.Button(root,text="Search",command=buttonclick)
button.pack(side="left")
text.pack(side="left")
listbox.pack(side="bottom",fill="both",expand=True)

root.mainloop()

