import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Load dataset
    try:
        df = pd.read_csv('train.csv')
        print("Dataset loaded successfully.")
    except FileNotFoundError:
        print("Error: train.csv not found in the current directory.")
        return

    # Data Cleaning
    print("Performing data cleaning...")
    # Fill missing Age with median
    df['Age'] = df['Age'].fillna(df['Age'].median())
    
    # Fill missing Embarked with mode
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    
    # Drop Cabin, Ticket, and Name columns
    df = df.drop(columns=['Cabin', 'Ticket', 'Name'], errors='ignore')

    # EDA Visualization
    print("Generating EDA visualizations...")
    
    # Set premium eye-catching dark aesthetic
    sns.set_theme(style="dark", font="sans-serif")
    plt.rcParams.update({
        'axes.facecolor': '#0D1117',
        'figure.facecolor': '#0D1117',
        'text.color': '#FFFFFF',
        'axes.labelcolor': '#A0AEC0',
        'axes.titlecolor': '#FFFFFF',
        'xtick.color': '#A0AEC0',
        'ytick.color': '#A0AEC0',
        'axes.edgecolor': '#2D3748'
    })
    
    # Eye-catching neon palette: Vibrant Neon Pink and Bright Cyan
    custom_palette = ["#FF3366", "#00E5FF"]
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Titanic Survival Analysis: Key Factors', fontsize=26, fontweight='black', color='#FFFFFF', y=0.98)

    # Helper function to add labels
    def add_labels(ax):
        for p in ax.patches:
            height = p.get_height()
            if height > 0:
                ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2., height),
                            ha='center', va='bottom', fontsize=12, fontweight='bold', color='#FFFFFF', xytext=(0, 6), textcoords='offset points')

    # Data formatting for human readability
    df['Survived_Label'] = df['Survived'].map({0: 'Did Not Survive', 1: 'Survived'})
    df['Pclass_Label'] = df['Pclass'].map({1: '1st Class', 2: '2nd Class', 3: '3rd Class'})

    # Plot 1: Count plot of overall survival
    sns.countplot(data=df, x='Survived_Label', hue='Survived_Label', ax=axes[0, 0], palette=custom_palette, order=['Did Not Survive', 'Survived'], legend=False)
    axes[0, 0].set_title('Overall Passenger Survival', fontsize=18, fontweight='bold', pad=15)
    axes[0, 0].set_xlabel('')
    axes[0, 0].set_ylabel('Number of Passengers', fontsize=14)
    add_labels(axes[0, 0])

    # Plot 2: Count plot of survival grouped by Sex
    sns.countplot(data=df, x='Sex', hue='Survived_Label', ax=axes[0, 1], palette=custom_palette, order=['male', 'female'])
    axes[0, 1].set_title('Survival Breakdown by Gender', fontsize=18, fontweight='bold', pad=15)
    axes[0, 1].set_xlabel('Passenger Gender', fontsize=14)
    axes[0, 1].set_ylabel('Number of Passengers', fontsize=14)
    axes[0, 1].legend(title='', fontsize=13, frameon=False, labelcolor='#FFFFFF')
    add_labels(axes[0, 1])

    # Plot 3: Count plot of survival grouped by Passenger Class (Pclass)
    sns.countplot(data=df, x='Pclass_Label', hue='Survived_Label', ax=axes[1, 0], palette=custom_palette, order=['1st Class', '2nd Class', '3rd Class'])
    axes[1, 0].set_title('Survival Based on Ticket Class', fontsize=18, fontweight='bold', pad=15)
    axes[1, 0].set_xlabel('Ticket Class', fontsize=14)
    axes[1, 0].set_ylabel('Number of Passengers', fontsize=14)
    axes[1, 0].legend(title='', fontsize=13, frameon=False, labelcolor='#FFFFFF')
    add_labels(axes[1, 0])

    # Plot 4: Stacked histogram of Age distribution colored by Survived
    sns.histplot(data=df, x='Age', hue='Survived_Label', multiple='stack', bins=30, ax=axes[1, 1], palette=custom_palette, edgecolor='#0D1117', linewidth=1.5)
    axes[1, 1].set_title('Age Distribution and Survival', fontsize=18, fontweight='bold', pad=15)
    axes[1, 1].set_xlabel('Age (Years)', fontsize=14)
    axes[1, 1].set_ylabel('Number of Passengers', fontsize=14)
    
    # Style the automatic legend created by histplot
    if axes[1, 1].get_legend() is not None:
        axes[1, 1].get_legend().set_title('')
        axes[1, 1].get_legend().set_frame_on(False)
        plt.setp(axes[1, 1].get_legend().get_texts(), color='#FFFFFF', fontsize=13)

    # Clean up spines and ticks
    for ax in axes.flat:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#2D3748')
        ax.spines['bottom'].set_color('#2D3748')
        ax.tick_params(axis='x', labelsize=12, color='#A0AEC0')
        ax.tick_params(axis='y', labelsize=12, color='#A0AEC0')
        ax.grid(axis='y', color='#2D3748', linestyle='--', alpha=0.6)

    # Layout adjustment
    plt.tight_layout(pad=3.0)

    # Save Image
    output_filename = 'titanic_eda_dashboard.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"Dashboard successfully saved as {output_filename}")

    # Output Key Insights to Console
    print("\n" + "="*50)
    print("📊 KEY PATTERNS & TRENDS IDENTIFIED:")
    print("="*50)
    print("1. Gender: Female passengers had a significantly higher survival rate than males.")
    print("2. Ticket Class: 1st-class passengers were much more likely to survive compared to 3rd-class.")
    print("3. Age Demographics: Younger passengers (especially children) had notably better survival outcomes.")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
