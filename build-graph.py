# README:
# to use this, open an empty graph in Gephi.  Go into Data Table -> Nodes and add the following columns:
#   * name
#   * type
#   * detail
#   * date
#
# now, go to Edges, and add the column 'type'
#
# finally, open a gephi command shell, and do
# execfile(<this file>)

def lookupNodeByName(name) :
  for n in g.nodes:
    if n['name'] == name:
      return n
  return None

def addEdgeByName(**args) :
  s = lookupNodeByName(args['source'])
  t = lookupNodeByName(args['target'])
  if args['type'] == "related to" :
    e = g.addUndirectedEdge(s, t)
  else :
    e = g.addDirectedEdge(s, t)
  e['type'] = args['type']
  return e

def addNodeToGraph(**args) :
  n = args['name']
  node = lookupNodeByName(n)
  if node is None:
    print args
    v = g.addNode(**args)
    v.Label = args['name']
    v.size = 36

addNodeToGraph(name="Donald Trump", type="person", detail="trump crime syndicate")
addNodeToGraph(name="Ivanka Trump", type="person", detail="trump crime syndicate")
addNodeToGraph(name="Jared Kushner", type="person", detail="trump crime syndicate")
addNodeToGraph(name="Eric Trump", type="person", detail="trump crime syndicate")
addNodeToGraph(name="Donald Trump, Jr.", type="person", detail="trump crime syndicate")
addNodeToGraph(name="Michael Cohen", type="person", detail="trump crime syndicate")
addNodeToGraph(name="Konstantin Kilimnik", type="person")
addNodeToGraph(name="Paul Manafort", type="person")
addNodeToGraph(name="Rick Gates", type="person")
addNodeToGraph(name="Michael Flynn", type="person")
addNodeToGraph(name="Sergey Kislyak", type="person")
addNodeToGraph(name="Natalya Veselnitskaya", type="person")
addNodeToGraph(name="Rob Goldstone", type="person")
addNodeToGraph(name="Vladimir Putin", type="person")
addNodeToGraph(name="Sergei Magnitsky", type="person")
addNodeToGraph(name="Aras Agalarov", type="person")
addNodeToGraph(name="Emin Agalarov", type="person")
addNodeToGraph(name="Rinat Akhmetshin", type="person")
addNodeToGraph(name="Tevfik Arif", type="person")
addNodeToGraph(name="Steve Bannon", type="person")
addNodeToGraph(name="Sam Clovis", type="person")
addNodeToGraph(name="James Comey", type="person")
addNodeToGraph(name="Oleg Deripaska", type="person")
addNodeToGraph(name="Herman Gref", type="person")
addNodeToGraph(name="Sean Hannity", type="person")
addNodeToGraph(name="Sergei Ivanov", type="person")
addNodeToGraph(name="Kassis", type="person")
addNodeToGraph(name="Sergey Lavrov", type="person")
addNodeToGraph(name="German Khan", type="person")
addNodeToGraph(name="Carter Page", type="person")
addNodeToGraph(name="George Papadapoulos", type="person")
addNodeToGraph(name="Dmitri Peskov", type="person")
addNodeToGraph(name="Erik Prince", type="person")
addNodeToGraph(name="Sapir", type="person")
addNodeToGraph(name="Felix Sater", type="person")
addNodeToGraph(name="Igor Sechin", type="person")
addNodeToGraph(name="Roger Stone", type="person")
addNodeToGraph(name="Aleksandr Torshin", type="person")
addNodeToGraph(name="Viktor Vekselberg", type="person")
addNodeToGraph(name="Viktor Yanukovich", type="person")
addNodeToGraph(name="v/d Zwaan", type="person")
addNodeToGraph(name="Ike Kaveladze", type="person")
addNodeToGraph(name="Frederick Intrater", type="person")
addNodeToGraph(name="Andrew Intrater", type="person")
addNodeToGraph(name="Andrey Artemenko", type="person")
addNodeToGraph(name="Bill Browder", type="person")
addNodeToGraph(name="Denis Katsyv", type="person")
addNodeToGraph(name="Pyotr Katsyv", type="person")
addNodeToGraph(name="Preet Bharara", type="person")
addNodeToGraph(name="Ahmed al-Rumaihi", type="person")
addNodeToGraph(name="Glenn Simpson", type="person")
addNodeToGraph(name="Ivan Glasenberg", type="person")

addNodeToGraph(name="Rusal", type="org", detail="state corp")
addNodeToGraph(name="Rosneft", type="org", detail="state corp")
addNodeToGraph(name="Manafort-Davis", type="org", detail="private")
addNodeToGraph(name="Renova Group", type="org", detail="state corp")
addNodeToGraph(name="Columbus Nova", type="org", detail="private")
addNodeToGraph(name="Prevezon Holdings", type="org", detail="private")
addNodeToGraph(name="Bayrock Group", type="org", detail="private")
addNodeToGraph(name="Novartis", type="org", detail="corp")
addNodeToGraph(name="Crocus Group", type="org", detail="private")
addNodeToGraph(name="KGB FSB", type="org", detail="government")
addNodeToGraph(name="EC LLC", type="org", detail="private")
addNodeToGraph(name="Internet Research Agency", type="org", detail="state corp")
addNodeToGraph(name="Miss Universe", type="org", detail="private")
addNodeToGraph(name="Deutsche Bank", type="org", detail="corp")
addNodeToGraph(name="AT&T", type="org", detail="corp")
addNodeToGraph(name="Human Rights Accountability Global Initiative", type="org", detail="bogus thinktank")
addNodeToGraph(name="Qatar Investment Authority", type="org", detail="state corp")
addNodeToGraph(name="Russian Railways", type="org", detail="state corp")
addNodeToGraph(name="Hermitage Capital Management", type="org", detail="corp")
addNodeToGraph(name="Fusion GPS", type="org", detail="corp")
addNodeToGraph(name="EN+", type="org", detail="corp")


addNodeToGraph(name="Trump Tower Meeting", type="meeting", date="20160609")
addNodeToGraph(name="Katsyv Fraud Scheme", type="meeting", date=" ")
addNodeToGraph(name="Peace Plan Meeting", type="meeting", date="20170131")
addNodeToGraph(name="Veselnitskaya-Simpson Meeting", type="meeting", date=" ")

addNodeToGraph(name="Magnitsky Act", type="law")

addNodeToGraph(name="New York", type="city")

## EDGES

#families
addEdgeByName(source="Donald Trump", type="related to", target="Ivanka Trump")
addEdgeByName(source="Donald Trump", type="related to", target="Eric Trump")
addEdgeByName(source="Donald Trump", type="related to", target="Donald Trump, Jr.")
addEdgeByName(source="Ivanka Trump", type="related to", target="Eric Trump")
addEdgeByName(source="Ivanka Trump", type="related to", target="Donald Trump, Jr.")
addEdgeByName(source="Eric Trump", type="related to", target="Donald Trump, Jr.")
addEdgeByName(source="Ivanka Trump", type="related to", target="Jared Kushner")
addEdgeByName(source="Viktor Vekselberg", type="related to", target="Frederick Intrater")
addEdgeByName(source="Viktor Vekselberg", type="related to", target="Andrew Intrater")
addEdgeByName(source="Frederick Intrater", type="related to", target="Andrew Intrater")
addEdgeByName(source="Emin Agalarov", type="related to", target="Aras Agalarov")
addEdgeByName(source="Pyotr Katsyv", type="related to", target="Denis Katsyv")

#money flow
addEdgeByName(source="AT&T", type="paid", target="EC LLC")
addEdgeByName(source="Novartis", type="paid", target="EC LLC")
addEdgeByName(source="Columbus Nova", type="paid", target="EC LLC")
addEdgeByName(source="Deutsche Bank", type="loaned money to", target="Jared Kushner")
addEdgeByName(source="Deutsche Bank", type="loaned money to", target="Donald Trump")
addEdgeByName(source="Crocus Group", type="paid", target="Miss Universe")
addEdgeByName(source="Igor Sechin", type="offered to pay", target="Carter Page")
addEdgeByName(source="Pyotr Katsyv", type="stole money from", target="Hermitage Capital Management")
addEdgeByName(source="Denis Katsyv", type="funds", target="Human Rights Accountability Global Initiative")
addEdgeByName(source="Denis Katsyv", type="stole money from", target="Katsyv Fraud Scheme")
addEdgeByName(source="Felix Sater", type="purchased real estate from", target="Donald Trump")
addEdgeByName(source="Qatar Investment Authority", type="purchased 19% of", target="Rosneft")
addEdgeByName(source="Qatar Investment Authority", type="tried to bribe", target="Steve Bannon")



# control and influence
addEdgeByName(source="Michael Cohen", type="controls", target="EC LLC")
addEdgeByName(source="Frederick Intrater", type="controls", target="Columbus Nova")
addEdgeByName(source="Renova Group", type="controls", target="Columbus Nova")
addEdgeByName(source="Viktor Vekselberg", type="controls", target="Renova Group")
addEdgeByName(source="Vladimir Putin", type="controls", target="KGB FSB")
addEdgeByName(source="Aras Agalarov", type="controls", target="Crocus Group")
addEdgeByName(source="Vladimir Putin", type="influences", target="Viktor Vekselberg")
addEdgeByName(source="Vladimir Putin", type="influences", target="Aras Agalarov")
addEdgeByName(source="Vladimir Putin", type="influences", target="Denis Katsyv")
addEdgeByName(source="Donald Trump", type="controls", target="Miss Universe")
addEdgeByName(source="Igor Sechin", type="controls", target="Rosneft")
addEdgeByName(source="Bill Browder", type="controls", target="Hermitage Capital Management")
addEdgeByName(source="Pyotr Katsyv", type="controls", target="Russian Railways")
addEdgeByName(source="Denis Katsyv", type="controls", target="Prevezon Holdings")
addEdgeByName(source="KGB FSB", type="controls", target="Internet Research Agency")
addEdgeByName(source="Tevfik Arif", type="controls", target="Bayrock Group")
addEdgeByName(source="Ivan Glasenberg", type="controls", target="Glencore")
addEdgeByName(source="Ivan Glasenberg", type="sat on board of", target="Rusal")
addEdgeByName(source="Oleg Deripaska", type="controls", target="EN+")
addEdgeByName(source="EN+", type="controls", target="Rusal")
addEdgeByName(source="QIA", type="owns 8.8% of", target="Glencore")


# employment and patronage
addEdgeByName(source="Michael Cohen", type="works for", target="Donald Trump")
addEdgeByName(source="Michael Flynn", type="worked for", target="Donald Trump")
addEdgeByName(source="Paul Manafort", type="worked for", target="Donald Trump")
addEdgeByName(source="Jared Kushner", type="works for", target="Donald Trump")
addEdgeByName(source="Steve Bannon", type="worked for", target="Donald Trump")
addEdgeByName(source="Carter Page", type="worked for", target="Donald Trump")
addEdgeByName(source="Roger Stone", type="worked for", target="Donald Trump")
addEdgeByName(source="Rick Gates", type="worked for", target="Michael Cohen")
addEdgeByName(source="Felix Sater", type="worked for", target="Donald Trump")
addEdgeByName(source="Felix Sater", type="worked for", target="Bayrock Group")
addEdgeByName(source="Bayrock Group", type="worked for", target="Donald Trump")
addEdgeByName(source="Andrew Intrater", type="works for", target="Columbus Nova")
addEdgeByName(source="Konstantin Kilimnik", type="worked for", target="KGB FSB")
addEdgeByName(source="Vladimir Putin", type="worked for", target="KGB FSB")
addEdgeByName(source="Paul Manafort", type="worked for", target="Viktor Yanukovich")
addEdgeByName(source="Rob Goldstone", type="works for", target="Emin Agalarov")
addEdgeByName(source="Rinat Akhmetshin", type="works for", target="KGB FSB")
addEdgeByName(source="Ike Kaveladze", type="works for", target="Crocus Group")
addEdgeByName(source="Carter Page", type="worked for", target="Donald Trump")
addEdgeByName(source="George Papadapoulos", type="worked for", target="Donald Trump")
addEdgeByName(source="Sam Clovis", type="worked for", target="Donald Trump")
addEdgeByName(source="Michael Cohen", type="works for", target="Sean Hannity")
addEdgeByName(source="Sergei Magnitsky", type="worked for", target="Bill Browder")
addEdgeByName(source="Rinat Akhmetshin", type="lobbies for", target="Human Rights Accountability Global Initiative")
addEdgeByName(source="Natalya Veselnitskaya", type="works for", target="Denis Katsyv")
addEdgeByName(source="Fusion GPS", type="works for", target="Denis Katsyv")
addEdgeByName(source="Natalya Veselnitskaya", type="works for", target="Pyotr Katsyv")
addEdgeByName(source="Pyotr Katsyv", type="worked for", target="KGB FSB")
addEdgeByName(source="Donald Trump", type="fired", target="Preet Bharara")
addEdgeByName(source="Ahmed al-Rumaihi", type="works for", target="Qatar Investment Authority")
addEdgeByName(source="Sergey Lavrov", type="works for", target="Vladimir Putin")


# meeting attendance
addEdgeByName(source="Jared Kushner", type="attended", target="Trump Tower Meeting")
addEdgeByName(source="Paul Manafort", type="attended", target="Trump Tower Meeting")
addEdgeByName(source="Rob Goldstone", type="attended", target="Trump Tower Meeting")
addEdgeByName(source="Natalya Veselnitskaya", type="attended", target="Trump Tower Meeting")
addEdgeByName(source="Donald Trump, Jr.", type="attended", target="Trump Tower Meeting")
addEdgeByName(source="Rinat Akhmetshin", type="attended", target="Trump Tower Meeting")
addEdgeByName(source="Natalya Veselnitskaya", type="attended", target="Veselnitskaya-Simpson Meeting")
addEdgeByName(source="Glenn Simpson", type="attended", target="Veselnitskaya-Simpson Meeting")
addEdgeByName(source="Felix Sater", type="attended", target="Peace Plan Meeting")
addEdgeByName(source="Michael Cohen", type="attended", target="Peace Plan Meeting")
addEdgeByName(source="Andrey Artemenko", type="attended", target="Peace Plan Meeting")


# support and detraction
addEdgeByName(source="Natalya Veselnitskaya", type="opposes", target="Magnitsky Act")
addEdgeByName(source="Igor Sechin", type="opposes", target="Magnitsky Act")
addEdgeByName(source="Human Rights Accountability Global Initiative", type="opposes", target="Magnitsky Act")

# misc
addEdgeByName(source="Denis Katsyv", type="prosecuted by", target="Preet Bharara")
addEdgeByName(source="Prevezon Holdings", type="bought real estate", target="New York")
addEdgeByName(source="Trump Tower Meeting", type="was about", target="Magnitsky Act")
addEdgeByName(source="Magnitsky Act", type="named after", target="Sergei Magnitsky")



# pairwise meetings
addEdgeByName(source="Michael Flynn", type = "met with", target="Vladimir Putin")
addEdgeByName(source="Michael Flynn", type = "met with", target="Sergey Kislyak")
addEdgeByName(source="Carter Page", type = "met with", target="Igor Sechin")
addEdgeByName(source="Michael Cohen", type = "met with", target="Ahmed al-Rumaihi")

