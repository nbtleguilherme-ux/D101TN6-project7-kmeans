"""
Project 7 — Customer Segmentation with K-Means
Dataset: Simulated retail customer behavior (seeded random)

No internet connection required. The script generates 300 synthetic customers
with 5 behavioral features across 4 hidden clusters, then saves to data/customers.csv.

Cluster design (for teacher reference — students do NOT have this label):
  Cluster 0 (Young Budget):    young, low income, moderate spending, frequent small buys
  Cluster 1 (High Value):      middle-aged, high income, high spending, infrequent large buys
  Cluster 2 (Senior Cautious): older, moderate income, low spending, rare transactions
  Cluster 3 (Mid Loyalists):   middle-aged, moderate income, moderate spending, frequent buys

Usage:
    pip install scikit-learn pandas numpy matplotlib
    python download_data.py
"""

import pathlib
import numpy as np
import pandas as pd

DATA_DIR = pathlib.Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "customers.csv"

RANDOM_SEED = 42
N_CUSTOMERS = 300


def generate_customers(seed: int = RANDOM_SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    # Each cluster: (n, age_mu, age_sd, income_mu, income_sd,
    #                score_mu, score_sd, freq_mu, freq_sd, txn_mu, txn_sd)
    clusters = [
        # Young Budget shoppers
        dict(n=75,  age=(24, 4),  income=(120, 20), score=(55, 12), freq=(22, 5), txn=(0.8, 0.2)),
        # High-Value customers
        dict(n=60,  age=(40, 8),  income=(480, 60), score=(82, 8),  freq=(8, 3),  txn=(4.5, 1.0)),
        # Senior Cautious buyers
        dict(n=80,  age=(58, 6),  income=(200, 35), score=(28, 10), freq=(5, 2),  txn=(1.2, 0.4)),
        # Mid Loyalists
        dict(n=85,  age=(34, 7),  income=(280, 40), score=(60, 10), freq=(16, 4), txn=(2.1, 0.5)),
    ]

    rows = []
    for cid, c in enumerate(clusters):
        n = c["n"]
        age            = rng.normal(*c["age"],   n).clip(18, 70).round().astype(int)
        annual_income  = rng.normal(*c["income"],n).clip(60, 700).round(1)
        spending_score = rng.normal(*c["score"], n).clip(0, 100).round(1)
        purchase_freq  = rng.normal(*c["freq"],  n).clip(1, 50).round().astype(int)
        avg_transaction= rng.normal(*c["txn"],   n).clip(0.2, 10).round(2)
        for i in range(n):
            rows.append({
                "age":             age[i],
                "annual_income":   annual_income[i],
                "spending_score":  spending_score[i],
                "purchase_freq":   purchase_freq[i],
                "avg_transaction": avg_transaction[i],
                # hidden label — strip before giving to students
                "_true_cluster":   cid,
            })

    df = pd.DataFrame(rows)
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    df.insert(0, "customer_id", range(1, len(df) + 1))
    return df


def validate(df: pd.DataFrame):
    errors = []
    if len(df) != N_CUSTOMERS:
        errors.append(f"  Expected {N_CUSTOMERS} rows, got {len(df)}")
    required_cols = ["customer_id", "age", "annual_income",
                     "spending_score", "purchase_freq", "avg_transaction"]
    for col in required_cols:
        if col not in df.columns:
            errors.append(f"  Missing column: {col}")
    if df[required_cols[1:]].isnull().any().any():
        errors.append("  Found NaN values in feature columns")
    if errors:
        print("[WARN] Validation issues:")
        for e in errors:
            print(e)
    else:
        print("[OK] Data validation passed.")


def print_stats(df: pd.DataFrame):
    features = ["age", "annual_income", "spending_score",
                "purchase_freq", "avg_transaction"]
    print(f"\n=== Dataset Statistics ===")
    print(f"  Rows: {len(df)}   Features: {len(features)}")
    print(f"\n  Descriptive statistics:")
    print(df[features].describe().round(2).to_string())
    print(f"\n  Correlation matrix (features):")
    print(df[features].corr().round(3).to_string())


def main():
    print(f"Generating {N_CUSTOMERS} synthetic customers (seed={RANDOM_SEED}) ...")
    df_full = generate_customers(RANDOM_SEED)

    validate(df_full)
    print_stats(df_full)

    # Save student-facing CSV (no true labels)
    student_cols = ["customer_id", "age", "annual_income",
                    "spending_score", "purchase_freq", "avg_transaction"]
    df_full[student_cols].to_csv(OUT_PATH, index=False)
    print(f"\n[OK] Saved to: {OUT_PATH}")
    print(f"     Columns: {student_cols}")

    print("""
Next steps in your notebook:
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    from sklearn.decomposition import PCA
    import matplotlib.pyplot as plt

    df = pd.read_csv("data/customers.csv")
    features = ["age", "annual_income", "spending_score",
                "purchase_freq", "avg_transaction"]
    X = StandardScaler().fit_transform(df[features])

    # Elbow method
    inertias = []
    for k in range(2, 11):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X)
        inertias.append(km.inertia_)
    plt.plot(range(2, 11), inertias, marker="o")
    plt.xlabel("K"); plt.ylabel("Inertia"); plt.title("Elbow Curve")
    plt.show()

    # Silhouette scores
    for k in range(2, 8):
        km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X)
        s = silhouette_score(X, km.labels_)
        print(f"K={k}  Silhouette={s:.4f}")

    # Final model + PCA visualization
    best_k = 4   # replace with your chosen K
    labels = KMeans(n_clusters=best_k, random_state=42, n_init=10).fit_predict(X)
    pcs = PCA(n_components=2).fit_transform(X)
    plt.scatter(pcs[:, 0], pcs[:, 1], c=labels, cmap="tab10", s=40)
    plt.title(f"K-Means (K={best_k}) — PCA projection")
    plt.show()
""")


if __name__ == "__main__":
    main()
