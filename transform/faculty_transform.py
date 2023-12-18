class Transform:
    def __init__(self, to, test) -> None:
        self.value = to
        self.test = test

def test(e, search):
    return any(s.lower() in e.lower() for s in search)

def transform_to_fstg(e):
    return test(e, ["FST", "FSTG", "Faculty of Sciences and Techniques"])

def transform_to_ensa(e):
    return test(e, ["ENSA"])

def transform_to_other(e):
    return e == "Université Cadi Ayyad"
    #return test(e, ["Université Cadi Ayyad", "Cadi Ayyad University", " Cadi  Ayyad"])

faculties_transform = [
    Transform("FSTG", transform_to_fstg),
    Transform("ENSA", transform_to_ensa),
    Transform("Other", transform_to_other),
]


def transform_faculties(data):
    for ind, item in enumerate(data):
        for transform in faculties_transform:
            if transform.test(item.get("ASS - Unevercity", "")):
                data[ind]["faculty"] = transform.value
                break
            else: data[ind]["faculty"] = "None"
 
        
if __name__ == "__main__":
    pass