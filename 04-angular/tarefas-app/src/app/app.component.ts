import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TarefaService, Tarefa } from './tarefa.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, FormsModule, CommonModule], 
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
// Implementar método adicionarTarefa()
  adicionarTarefa() {
    // Verifica se o título não está vazio ou contém apenas espaços em branco
    if (this.novoTitulo.trim()) {
      // Usa o serviço para adicionar a nova tarefa, passando o título sem espaços extras
      this.tarefaService.adicionarTarefa(this.novoTitulo.trim());
      
      // Limpa a propriedade, o que também limpa o campo de input no HTML
      this.novoTitulo = '';
    }
  }

  // TODO: Implementar método toggleConcluida(id: number)
  toggleConcluida(id: number) {
    // TODO: Usar toggleConcluida(id) do tarefaService
    this.tarefaService.toggleConcluida(id);
  }

  // TODO: Implementar método removerTarefa(id: number)
  removerTarefa(id: number) {
    // TODO: Usar removerTarefa(id) do tarefaService
    this.tarefaService.removerTarefa(id);
  }

  // TODO: Implementar método filtrarTarefas()
  filtrarTarefas(): Tarefa[] {
    // TODO: Usar filtrarTarefas(this.filtroAtual) do tarefaService
    // TODO: Retornar array filtrado
    return this.tarefaService.filtrarTarefas(this.filtroAtual);
  }

  // TODO: Implementar método contarPendentes()
  contarPendentes(): number {
    // TODO: Usar contarPendentes() do tarefaService
    return this.tarefaService.contarPendentes();
  }
}
