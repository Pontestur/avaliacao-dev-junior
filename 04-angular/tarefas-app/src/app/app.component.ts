import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TarefaService, Tarefa } from './tarefa.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, FormsModule], 
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  // TODO: Propriedade para novo título da tarefa
  novoTitulo = '';

  // TODO: Propriedade para filtro atual
  filtroAtual: 'todas' | 'pendentes' | 'concluidas' = 'todas';

  // TODO: Injetar TarefaService no constructor
  constructor(private tarefaService: TarefaService) {}

  // TODO: Implementar método adicionarTarefa()
  adicionarTarefa() {
    // TODO: Usar adicionarTarefa(novoTitulo) do tarefaService
    // TODO: Limpar novoTitulo após adicionar
  }

  // TODO: Implementar método toggleConcluida(id: number)
  toggleConcluida(id: number) {
    // TODO: Usar toggleConcluida(id) do tarefaService
  }

  // TODO: Implementar método removerTarefa(id: number)
  removerTarefa(id: number) {
    // TODO: Usar removerTarefa(id) do tarefaService
  }

  // TODO: Implementar método filtrarTarefas()
  filtrarTarefas(): Tarefa[] {
    // TODO: Usar filtrarTarefas(this.filtroAtual) do tarefaService
    // TODO: Retornar array filtrado
    return [];
  }

  // TODO: Implementar método contarPendentes()
  contarPendentes(): number {
    // TODO: Usar contarPendentes() do tarefaService
    return 0;
  }
}
