import { Injectable } from '@angular/core';

export interface Tarefa {
  id: number;
  titulo: string;
  concluida: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class TarefaService {
  private tarefas: Tarefa[] = [
    { id: 1, titulo: 'Estudar Angular', concluida: false },
    { id: 2, titulo: 'Fazer exercícios de TypeScript', concluida: true },
    { id: 3, titulo: 'Implementar componentes', concluida: false },
    { id: 4, titulo: 'Aprender sobre Services', concluida: false },
    { id: 5, titulo: 'Praticar data binding', concluida: true }
  ];

  // Retorna todas as tarefas
  getTarefas(): Tarefa[] {
    return [...this.tarefas]; // Retorna uma cópia para evitar modificações diretas
  }

  // Adiciona uma nova tarefa
  adicionarTarefa(titulo: string): void {
    if (titulo.trim()) {
      const novaTarefa: Tarefa = {
        id: this.gerarNovoId(),
        titulo: titulo.trim(),
        concluida: false
      };
      this.tarefas.push(novaTarefa);
    }
  }

  // Alterna o status de conclusão de uma tarefa
  toggleConcluida(id: number): void {
    const tarefa = this.tarefas.find(t => t.id === id);
    if (tarefa) {
      tarefa.concluida = !tarefa.concluida;
    }
  }

  // Remove uma tarefa pelo ID
  removerTarefa(id: number): void {
    const index = this.tarefas.findIndex(t => t.id === id);
    if (index > -1) {
      this.tarefas.splice(index, 1);
    }
  }

  // Filtra tarefas por status
  filtrarTarefas(filtro: 'todas' | 'pendentes' | 'concluidas'): Tarefa[] {
    const todasTarefas = this.getTarefas();

    switch (filtro) {
      case 'pendentes':
        return todasTarefas.filter(t => !t.concluida);
      case 'concluidas':
        return todasTarefas.filter(t => t.concluida);
      default:
        return todasTarefas;
    }
  }

  // Conta o número de tarefas pendentes
  contarPendentes(): number {
    return this.tarefas.filter(t => !t.concluida).length;
  }

  // Gera um novo ID único
  private gerarNovoId(): number {
    return this.tarefas.length > 0
      ? Math.max(...this.tarefas.map(t => t.id)) + 1
      : 1;
  }
}