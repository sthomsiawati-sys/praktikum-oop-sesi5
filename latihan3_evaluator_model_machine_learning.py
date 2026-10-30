"""Latihan Praktikum 3: Evaluator Model Machine Learning (Duck Typing). 
Tiga class di bawah ini TIDAK memiliki parent class yang sama. Fungsi run_model_evaluation() hanya peduli apakah objek punya metode evaluate_performance(), bukan class asalnya (Duck Typing)."""

import math

class RegressionModel:
    """Model regresi: metrik MSE, RMSE, dan MAE."""

    def __init__(self, name: str = "Linear Regression"):
        self.name = name

    def predict(self, x_test: list) -> list:
        # Model sederhana: y = 2x + 1
        return [2 * x + 1 for x in x_test]

    def evaluate_performance(self, x_test, y_test) -> dict:
        y_pred = self.predict(x_test)
        n = len(y_test)
        mse = sum((a - b) ** 2 for a, b in zip(y_test, y_pred)) / n
        mae = sum(abs(a - b) for a, b in zip(y_test, y_pred)) / n
        return {"model": self.name, "MSE": round(mse, 4),
                "RMSE": round(math.sqrt(mse), 4), "MAE": round(mae, 4)}

class ClassificationModel:
    """Model klasifikasi: metrik Accuracy."""

    def __init__(self, name: str = "Threshold Classifier",
                 threshold: float = 5.0):
        self.name = name
        self.threshold = threshold

    def predict(self, x_test: list) -> list:
        return [1 if x >= self.threshold else 0 for x in x_test]

    def evaluate_performance(self, x_test, y_test) -> dict:
        y_pred = self.predict(x_test)
        benar = sum(1 for a, b in zip(y_test, y_pred) if a == b)
        return {"model": self.name,
                "Accuracy": round(benar / len(y_test), 4),
                "Benar": benar, "Total": len(y_test)}

class ClusteringModel:
    """Model clustering 1 dimensi: metrik Silhouette Score. y_test berisi label cluster hasil prediksi/penugasan"""

    def __init__(self, name: str = "Simple Clustering"):
        self.name = name

    @staticmethod
    def _dist(a: float, b: float) -> float:
        return abs(a - b)

    def evaluate_performance(self, x_test, y_test) -> dict:
        n = len(x_test)
        scores = []
        for i in range(n):
            same = [self._dist(x_test[i], x_test[j]) for j in range(n)
                    if j != i and y_test[j] == y_test[i]]
            a = sum(same) / len(same) if same else 0.0
            b = math.inf
            for c in set(y_test):
                if c == y_test[i]:
                    continue
                other = [self._dist(x_test[i], x_test[j]) for j in range(n)
                         if y_test[j] == c]
                b = min(b, sum(other) / len(other))
            denom = max(a, b)
            scores.append((b - a) / denom if denom > 0 and b != math.inf
                          else 0.0)
        return {"model": self.name,
                "Silhouette Score": round(sum(scores) / n, 4),
                "Jumlah Cluster": len(set(y_test))}

def run_model_evaluation(model_instance, x_data, y_data):
    """Fungsi independen berbasis Duck Typing."""
    print(f"=== EVALUASI: {type(model_instance).__name__} ===")
    if not hasattr(model_instance, "evaluate_performance"):
        print("[ERROR] Objek tidak memiliki evaluate_performance()")
        return None
    hasil = model_instance.evaluate_performance(x_data, y_data)
    for kunci, nilai in hasil.items():
        print(f"  {kunci}: {nilai}")
    print("-" * 50)
    return hasil

class BukanModel:
    """Objek tanpa evaluate_performance, untuk menguji penanganan error."""

def main():
    x_reg, y_reg = [1, 2, 3, 4, 5], [3.2, 4.8, 7.1, 9.3, 10.9]
    run_model_evaluation(RegressionModel(), x_reg, y_reg)

    x_cls, y_cls = [1, 3, 5, 7, 9, 2], [0, 0, 1, 1, 1, 1]
    run_model_evaluation(ClassificationModel(), x_cls, y_cls)

    x_clu = [1.0, 1.2, 0.8, 8.0, 8.5, 7.9]
    y_clu = [0, 0, 0, 1, 1, 1]
    run_model_evaluation(ClusteringModel(), x_clu, y_clu)

    run_model_evaluation(BukanModel(), x_reg, y_reg)

if __name__ == "__main__":
    main()
