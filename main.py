# Importando as bibliotecas necessárias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando o dataset
df = pd.read_csv('nba_per_game_processed.csv')

# 1. Resumo estatístico dos dados
print("Resumo estatístico dos dados:")
print(df.describe())

# 2. Top 10 jogadores com maior média de pontos
print("\nTop 10 jogadores com maior média de pontos:")
top_10_scorers = df.nlargest(10, 'PTS')
print(top_10_scorers[['Player Name', 'PTS']])

# 3. Distribuição da idade dos jogadores
sns.histplot(df['Age'], kde=True)
plt.title('Distribuição da Idade dos Jogadores')
plt.xlabel('Idade')
plt.ylabel('Número de Jogadores')
plt.show()

# 4. Correlação entre tentativas e eficiência de arremessos
sns.scatterplot(data=df, x='FGA', y='FG%')
plt.title('Correlação entre Tentativas de Arremesso e Eficiência')
plt.xlabel('Tentativas de Arremesso (FGA)')
plt.ylabel('Eficiência de Arremesso (FG%)')
plt.show()

# 5. Médias de pontos por time
team_points = df.groupby('Team')['PTS'].mean().sort_values(ascending=False)
team_points.plot(kind='bar')
plt.title('Média de Pontos por Time')
plt.xlabel('Time')
plt.ylabel('Média de Pontos')
plt.show()

# 6. Eficiência de arremessos em relação à posição dos jogadores
sns.boxplot(data=df, x='Position', y='FG%')
plt.title('Eficiência de Arremessos por Posição')
plt.xlabel('Posição')
plt.ylabel('Eficiência de Arremesso (FG%)')
plt.show()

# 7. Relação entre Assistências e Pontos
sns.scatterplot(data=df, x='AST', y='PTS')
plt.title('Relação entre Assistências e Pontos')
plt.xlabel('Assistências por Jogo')
plt.ylabel('Pontos por Jogo')
plt.show()

# 8. Eficiência de arremessos de três pontos por time
team_3P_efficiency = df.groupby('Team')['3P%'].mean().sort_values(ascending=False)
team_3P_efficiency.plot(kind='bar')
plt.title('Eficiência de Arremessos de Três Pontos por Time')
plt.xlabel('Time')
plt.ylabel('Eficiência de Três Pontos (3P%)')
plt.show()

# 9. Top 5 jogadores em termos de rebotes ofensivos e defensivos
top_ORB = df.nlargest(5, 'ORB')[['Player Name', 'ORB']]
top_DRB = df.nlargest(5, 'DRB')[['Player Name', 'DRB']]
print("\nTop 5 jogadores em rebotes ofensivos:")
print(top_ORB)
print("\nTop 5 jogadores em rebotes defensivos:")
print(top_DRB)

# 10. Distribuição de Bloqueios por Posição
sns.boxplot(data=df, x='Position', y='BLK')
plt.title('Distribuição de Bloqueios por Posição')
plt.xlabel('Posição')
plt.ylabel('Bloqueios por Jogo (BPG)')
plt.show()