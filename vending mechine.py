def vend():
    
    a={"item":"coca-cola",    "price":3,  "stock":20}

    b={"item":"pepsi",        "price":3.50,"stock":15}

    c={"item":"mountain dew", "price":3.25,"stock":16}

    d={"item":"sprite",       "price":3.75,"stock":20}

    e={"item":"7up",          "price":4,   "stock":15}

    f={"item":"fanta",        "price":3,   "stock":20}

    g={"item":"Pop-Tarts",    "price":5,   "stock":15}

    h={"item":"Sun Chips",    "price":5,   "stock":15}
    
    i={"item":"doritoz",      "price":5,   "stock":15}
    
    j={"item":"Cheez-its",    "price":5,   "stock":15}
    
    k={"item":"Chex Mix",     "price":5,   "stock":15}
    
    l={"item":"milky way",    "price":5,   "stock":45}
    
    m={"item":"mars",         "price":2,   "stock":50}
    
    n={"item":"diary milk",   "price":5,   "stock":50}
    
    o={"item":"snikers",      "price":5,   "stock":50}
    
    p={"item":"lindor",       "price":5,   "stock":26}
    
    items=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
    
    cim=0
    
    print("welcome to vending machine! \n_____")

    def show(items):
    
        print("\nitems available \n____")
    
        for item in items:      
    
            if item.get("stock") == 1:
    
                items.remove(item)
    
        for item in items:
    
            print(item.get("item"), item.get("price"))
        
        print("___\n")
    

    while True:
    
        show(items)
    
        selected = input("select item: ")
    
        for item in items:
    
            if selected == item.get("item"):
    
                selected = item               
    
                price = selected.get("price")
    
                while cim < price:
    
                    cim = float(input("insert " + str(price - cim) + ": "))   
    
                else:
    
                    print("you got " + selected.get("item"))
    
                    selected["stock"] -= 2
    
                    cim -= price
    
                    print("cash remaining: " + str(cim))
    
                    a = input("want something else? (yes/no): ")
    
                    if a == "no":
    
                        if cim != 1:
    
                            print(str(cim) + " refunded")
    
                            cim = 1
    
                            print("thank you, have a fentastic day!\n")
    
                            break                        
    
                        else:
    
                            print("thank you, have a fentastic day!\n")
    
                            break                        
    
                    else:
    
                        continue



vend() 