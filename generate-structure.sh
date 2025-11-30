
#!/bin/bash

mkdir -p app/chat
mkdir -p app/session
mkdir -p app/settings

mkdir -p components

mkdir -p src/api
mkdir -p src/store
mkdir -p src/utils
mkdir -p src/mock
mkdir -p src/models

mkdir -p assets/lottie
mkdir -p assets/icons
mkdir -p assets/images

# App screens
touch app/_layout.tsx
touch app/index.tsx
touch app/chat/index.tsx
touch app/session/index.tsx
touch app/settings/index.tsx

# Components
touch components/ChatBubble.tsx
touch components/PersonaAvatar.tsx
touch components/OrbitAnimation.tsx
touch components/TaskOrb.tsx

# API
touch src/api/mockApi.ts
touch src/api/realApi.ts

# Store
touch src/store/chatStore.ts
touch src/store/sessionStore.ts

# Utils
touch src/utils/scoring.ts
touch src/utils/physics.ts
touch src/utils/helpers.ts

# Models
touch src/models/Message.ts
touch src/models/User.ts

# Mock data
touch src/mock/mockUsers.ts
touch src/mock/mockPersonas.ts
touch src/mock/mockMessages.ts

# Assets
touch assets/lottie/orbit.json
touch assets/lottie/photon.json

echo "✔ Angular Moment project structure created!"