class Model:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def accuracy_score(self):
        print('calculating...')
        self.accuracy = sum([i == j for i, j in zip(
            self.y_true, self.y_pred)])/len(self.y_true)
        print(f"model accuracy: {self.accuracy:.4f}")


model = Model([0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0])

model.accuracy_score()
