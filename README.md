
# Dog cross 🐶🚗

Um jogo desenvolvido com Python e Pygame inspirado no jogo Crossy Road, onde o jogador controla um cachorro tentando atravessar ruas, trilhos e gramados evitando obstáculos como carros e trens.

## 👥 Autores
- Andre Tostes, Eduardo Alba, Rafael Penhas

## 📁 Estrutura do Projeto

```
crossy_dog/
├── main.py                # Arquivo principal que roda o jogo
├── config.py              # Constantes e tamanhos da tela e sprites
├── assets.py              # Carregamento de imagens e sons
├── Assets/                # Pasta com imagens e sons usados no jogo
│   ├── Armature_jumping_left_1.png
│   ├── Armature_jumping_right_1.png
│   ├── player_dead.png
│   ├── collision.wav
│   └── ...
└── README.md              # Este arquivo
```

## ▶️ Como executar o jogo

1. Instale as dependências:
```bash
pip install pygame
```

2. Rode o jogo com:
```bash
python main.py
```

Exigências:
- Python 3.8+
- Biblioteca `pygame`

## 🎮 Controles

- **↑ (Seta para cima):** mover para frente 
- **↓ (Seta para baixo):** mover para trás
- **← / → (Setas laterais):** mover lateralmente
- **ESC:** sair do jogo
- **Espaço (tela inicial):** iniciar o jogo
- **R (tela de game over):** reiniciar

## 🧠 Funcionalidades

- Pontuação aumenta a cada passo para frente
- Som de colisão ao bater em carro ou trem
- Animação de morte com sprite caído
- Sistema de inatividade (cachorro morre se não se mover)
- Terrenos variados (grama, rua, trilho)
- Sistema que evita muitas ruas seguidas para manter jogabilidade justa`

## 🖼️ Referências de Assets

- Música: *Bit Quest* - Kevin MacLeod
- Imagens isométricas geradas via IA (DALL·E e edição manual)
- Sons de colisão personalizados
- Outros recursos gráficos retirados de:
  - https://opengameart.org
  - https://kenney.nl/assets

