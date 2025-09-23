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
    // TODO: Usar this.tarefaService.adicionarTarefa(this.novoTitulo)
    // TODO: Limpar novoTitulo após adicionar
  }

  // TODO: Implementar método toggleConcluida(id: number)
  toggleConcluida(id: number) {
    // TODO: Usar this.tarefaService.toggleConcluida(id)
  }

  // TODO: Implementar método removerTarefa(id: number)
  removerTarefa(id: number) {
    // TODO: Usar this.tarefaService.removerTarefa(id)
  }

  // TODO: Implementar método filtrarTarefas()
  filtrarTarefas(): Tarefa[] {
    // TODO: Usar this.tarefaService.filtrarTarefas(this.filtroAtual)
    // TODO: Retornar array filtrado
    return [];
  }

  // TODO: Implementar método contarPendentes()
  contarPendentes(): number {
    // TODO: Usar this.tarefaService.contarPendentes()
    return 0;
  }
}
