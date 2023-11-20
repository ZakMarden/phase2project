class GrammarStats:
    def __init__(self):
        self.blank_list = []
        self.trues = 0
        self.falses = 0

 
    def check(self,*texts):
        for text in texts:
            self.blank_list.append(text)
            if text[0].isupper() and text[-1] in ".!?":
                self.trues += 1
            else:
                self.falses += 1
    
        

    def percentage_good(self):
        return (self.trues) / (self.falses + self.trues) * 100



test = GrammarStats()

test.check("aaaa","Aaaaa.","aaaa","aaaa","aaaa","aaaa","aaaa","aaaa","aaaa","aaaa",)
# test.check("Aaaa.")

# print(test.trues)

print(test.percentage_good())

