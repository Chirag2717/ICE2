version: 0.2
phases:
  install:
    commands:
      - npm install
  build:
    commands:
      - echo "Build completed"
artifacts:
  files:
    - '**/*'
