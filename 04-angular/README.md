# Exercício Angular - Sistema de Tarefas (40 minutos)

## Funcionalidades a implementar:

### 1. Lista de Tarefas (10 pts)
- Exibir tarefas usando *ngFor
- Mostrar: título, descrição, prioridade, data limite
- Visual diferente para tarefas concluídas

### 2. Adicionar Nova Tarefa (12 pts)
- Formulário reativo com validação
- Campos: título (obrigatório), descrição, prioridade, data limite
- Botão salvar desabilitado se inválido

### 3. Filtros e Busca (10 pts)  
- Filtrar: Todas / Pendentes / Concluídas
- Campo de busca por título/descrição
- Contador de pendentes

### 4. Ações nas Tarefas (8 pts)
- Marcar como concluída/pendente
- Remover tarefa
- Editar tarefa existente (opcional: +3 pts extras)

## Como começar:
1. O componente base já foi criado
2. Implemente as funcionalidades nos arquivos fornecidos
3. Use os dados de teste já incluídos
4. Execute `ng serve` para testar

## Arquivos para modificar:
- `src/app/tarefas/tarefas.component.ts`
- `src/app/tarefas/tarefas.component.html` 
- `src/app/tarefas/tarefas.component.css`
