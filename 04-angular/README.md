# Avaliação Técnica - Parte 4: Angular

## Visão Geral
Exercício prático de Angular focado em conceitos fundamentais: componentes, data binding, diretivas e eventos. Tempo estimado: **1-2 horas**.

## Objetivo
Criar uma **Lista de Tarefas** simples implementando funcionalidades básicas do Angular no componente principal da aplicação.

## Estrutura do Projeto
```
04-angular/
└── tarefas-app/                    # Aplicação Angular
    ├── src/app/
    │   ├── app.component.ts        # ARQUIVO PRINCIPAL - IMPLEMENTAR AQUI
    │   ├── app.component.html      # TEMPLATE - IMPLEMENTAR AQUI
    │   ├── app.component.css       # ESTILOS - IMPLEMENTAR AQUI
    │   ├── tarefa.service.ts       # SERVICE PRONTO - USAR NOS EXERCÍCIOS
    │   └── app.config.ts           # Configuração (não alterar)
    ├── package.json
    └── README.md
```

## Tecnologias Utilizadas
- **Angular 18** - Framework
- **TypeScript** - Linguagem
- **CSS3** - Estilização

## Estrutura Base Já Criada

O projeto Angular já contém:
- **Interface Tarefa** definida no `app.component.ts`
- **Projeto Angular** totalmente configurado
- **Dependências** pré-instaladas
- **Estrutura base** dos componentes

**Você precisa implementar:**
- Lógica no `app.component.ts`
- Template no `app.component.html`
- Estilos no `app.component.css`

## Exercícios a Implementar

### 1. Injeção de Dependência (5 pontos)
No `app.component.ts`:
- Importar `TarefaService` e interface `Tarefa`
- Injetar o service no constructor
- Propriedades para filtro e novo título já estão criadas

### 2. Template da Lista (15 pontos)
No `app.component.html`, criar:
- **Lista que exibe todas as tarefas** vindas do método `filtrarTarefas()`
- **Cada tarefa deve mostrar**: título e checkbox/botão para marcar como concluída
- **Tarefas concluídas** devem ter aparência visual diferente (riscado/opaco)
- **Contador no topo** mostrando quantas tarefas estão pendentes
- **Botão "Remover"** para cada tarefa individual

### 3. Formulário para Adicionar (15 pontos)
No template, criar:
- **Campo de texto** onde o usuário digita o título da nova tarefa
- **Botão "Adicionar"** que ao ser clicado adiciona a tarefa na lista
- **Campo deve ficar limpo** após adicionar uma tarefa
- **Nova tarefa deve aparecer imediatamente** na lista após ser adicionada

### 4. Marcar como Concluída (10 pontos)
Funcionalidade para alternar status:
- **Clicar no checkbox/botão** de uma tarefa pendente → ela fica concluída
- **Clicar no checkbox/botão** de uma tarefa concluída → ela volta a pendente
- **Visual deve mudar imediatamente** (riscado/opaco vs normal)
- **Contador de pendentes** deve atualizar automaticamente

### 5. Filtros Simples (10 pontos)
Implementar 3 botões de filtro:
- **Botão "Todas"**: mostra todas as tarefas (pendentes + concluídas)
- **Botão "Pendentes"**: mostra apenas tarefas não concluídas
- **Botão "Concluídas"**: mostra apenas tarefas concluídas
- **Lista deve atualizar** imediatamente ao clicar em qualquer filtro

### 6. Remover Tarefa (5 pontos)
Funcionalidade de exclusão:
- **Botão "Remover"** ao lado de cada tarefa
- **Clicar no botão** → tarefa some da lista imediatamente
- **Contador** deve atualizar se a tarefa removida era pendente

## Como Executar

1. **Navegar para o diretório:**
   Execute no terminal:
   ```
   cd 04-angular/tarefas-app
   ```

2. **Instalar dependências:**
   Execute no terminal:
   ```
   npm install
   ```

3. **Executar aplicação:**
   Execute no terminal:
   ```
   ng serve
   # ou
   npm start
   ```

4. **Abrir no navegador:**
   ```
   http://localhost:4200
   ```

## Estrutura Base para Implementar

### Estrutura Base (app.component.ts)
```typescript
interface Tarefa {
  id: number;
  titulo: string;
  concluida: boolean;
}

export class AppComponent {
  tarefas: Tarefa[] = [];
  novoTitulo = '';
  filtroAtual: 'todas' | 'pendentes' | 'concluidas' = 'todas';

  // TODO: Implementar métodos aqui
  adicionarTarefa() {
    // Implementar lógica
  }

  // TODO: Implementar outros métodos
}
```

### Estrutura HTML Necessária

O template deve conter estes **4 elementos principais**:

#### 1. **Seção de Formulário**
- Campo input para digitar título da nova tarefa
- Botão "Adicionar" para criar a tarefa

#### 2. **Seção de Filtros**
- 3 botões: "Todas", "Pendentes", "Concluídas"
- Deve alterar qual lista de tarefas é exibida

#### 3. **Contador de Pendentes**
- Texto mostrando quantas tarefas ainda não foram concluídas
- Deve atualizar automaticamente

#### 4. **Lista de Tarefas**
- Exibir cada tarefa da lista filtrada
- Para cada tarefa mostrar: título, botão/checkbox concluir, botão remover
- Tarefas concluídas devem ter visual diferente

## Métodos a Implementar

1. `adicionarTarefa()` - Adiciona nova tarefa à lista
2. `toggleConcluida(id: number)` - Alterna status de conclusão
3. `removerTarefa(id: number)` - Remove tarefa da lista
4. `filtrarTarefas()` - Retorna lista filtrada conforme filtro atual
5. `contarPendentes()` - Conta tarefas não concluídas
6. `gerarId()` - Gera ID único para novas tarefas

## Critérios de Avaliação

### Funcionalidade (50 pontos)
- ✅ Interface Tarefa criada corretamente
- ✅ Lista exibe tarefas com *ngFor
- ✅ Adicionar nova tarefa funciona
- ✅ Marcar como concluída funciona
- ✅ Filtros funcionam corretamente
- ✅ Remover tarefa funciona

### Conceitos Angular (30 pontos)
- ✅ Data binding correto (interpolação, property binding)
- ✅ Event binding para cliques
- ✅ Two-way binding com ngModel
- ✅ Uso correto de diretivas (*ngFor, *ngIf, ngClass)

### Interface e Organização (20 pontos)
- ✅ Layout limpo e organizado
- ✅ CSS para estados diferentes (concluída/pendente)
- ✅ Código TypeScript bem estruturado
- ✅ Nomes de métodos e propriedades claros

## Dicas de Implementação

### 1. Para usar ngModel, adicionar no app.component.ts:
```typescript
import { FormsModule } from '@angular/forms';

@Component({
  // ...
  imports: [FormsModule],
  // ...
})
```

### 2. Exemplo de método simples:
```typescript
adicionarTarefa() {
  if (this.novoTitulo.trim()) {
    this.tarefas.push({
      id: this.gerarId(),
      titulo: this.novoTitulo,
      concluida: false
    });
    this.novoTitulo = '';
  }
}
```

### 3. CSS básico para estados:
```css
.tarefa-concluida {
  text-decoration: line-through;
  opacity: 0.6;
}

.tarefa-pendente {
  font-weight: bold;
}
```

## Entrega

Implementar todas as funcionalidades nos arquivos:
- `src/app/app.component.ts`
- `src/app/app.component.html`
- `src/app/app.component.css`

**Total de pontos: 60**
**Tempo estimado: 1-2 horas**
**Nível: Básico a Intermediário**

---

**Boa sorte! 🚀**
