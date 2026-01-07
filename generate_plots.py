import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.dpi'] = 300

def safe_plot():
    # 1. Overload Plot
    try:
        df = pd.read_csv('results_overload.csv')
        fig, ax1 = plt.subplots(figsize=(6, 4))
        ax1.set_xlabel('Step')
        ax1.set_ylabel('Queue Length', color='tab:red')
        ax1.plot(df['step'], df['queue_len'], color='tab:red', label='Queue')
        ax1.tick_params(axis='y', labelcolor='tab:red')
        
        ax2 = ax1.twinx()
        ax2.set_ylabel('Entropy (Bits)', color='tab:blue')
        ax2.plot(df['step'], df['mean_ent'], color='tab:blue', linestyle='--', label='Entropy')
        ax2.tick_params(axis='y', labelcolor='tab:blue')
        
        plt.title('Exp 1: System Saturation')
        plt.tight_layout()
        plt.savefig('figure_1_overload.png')
        print("✅ Figure 1 saved.")
    except Exception as e:
        print(f"Exp 1 Error: {e}")

    # 2. Scaling Plot
    try:
        df = pd.read_csv('results_scaling.csv')
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(df['n'].astype(str), df['mean_firing_rate'], color='gray')
        ax.set_xlabel('Network Size (N)')
        ax.set_ylabel('Mean Firing Rate (Hz)')
        ax.set_title('Exp 2: Emergent Activity vs Scale')
        plt.tight_layout()
        plt.savefig('figure_2_scaling.png')
        print("✅ Figure 2 saved.")
    except Exception as e:
        print(f"Exp 2 Error: {e}")

    # 3. Ablation Plot
    try:
        df = pd.read_csv('results_ablation.csv')
        plt.figure(figsize=(6, 4))
        plt.plot(df['step'], df['links_control'], label='Plasticity Enabled', color='green')
        plt.plot(df['step'], df['links_ablated'], label='Fixed Topology', color='red', linestyle='--')
        plt.ylim(2480, 2510)
        plt.xlabel('Step')
        plt.ylabel('Connection Count')
        plt.legend()
        plt.title('Exp 3: Short-Term Structural Stability')
        plt.tight_layout()
        plt.savefig('figure_3_ablation.png')
        print("✅ Figure 3 saved.")
    except Exception as e:
        print(f"Exp 3 Error: {e}")

if __name__ == "__main__":
    safe_plot()
