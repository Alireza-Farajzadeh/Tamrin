class CustomStr:
    def __init__(self, string):
        self.string = string

    def custom_split(self, *splits):
        split_string = [self.string]
        for i in splits:
            a = []
            for q in split_string:
                a.extend(q.split(i))
            split_string = a

        return split_string
