import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Tarefa } from '../models/tarefa';

@Component({
  selector: 'app-tarefas',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './tarefas.component.html',
  styleUrls: ['./tarefas.component.css']
})
export class TarefasComponent {
  filtroAtual = 'todas';
  textoBusca = '';
  
  // Formulário para nova tarefa - JÁ CONFIGURADO
  tarefaForm: FormGroup;

  // Dados de teste - NÃO MODIFICAR
  tarefas: Tarefa[] = [
    {
      id: 1,
      titulo: 'Estudar Angular',
      descricao: 'Completar exercício de componentes',
      concluida: false,
      prioridade: 'alta',
      dataLimite: '2024-12-30',
      dataCriacao: '2024-09-19'
    },
    {
      id: 2,
      titulo: 'Fazer compras',
      descricao: 'Comprar ingredientes para jantar',
      concluida: true,
      prioridade: 'media',
      dataLimite: '2024-09-20',
      dataCriacao: '2024-09-18'
    },
    {
      id: 3,
      titulo: 'Exercício físico',
      descricao: 'Corrida de 30 minutos no parque',
      concluida: false,
      prioridade: 'baixa',
      dataLimite: '2024-09-21',
      dataCriacao: '2024-09-19'
    }
  ];

  constructor(private fb: FormBuilder) {
    // Configuração do formulário - JÁ IMPLEMENTADO
    this.tarefaForm = this.fb.group({
      titulo: ['', [Validators.required, Validators.minLength(3)]],
      descricao: ['', Validators.required],
      prioridade: ['media', Validators.required],
      dataLimite: ['', Validators.required]
    });
  }

  // TODO 1: Implementar getter para tarefas filtradas
  get tarefasFiltradas(): Tarefa[] {
    // IMPLEMENTAR: filtrar tarefas baseado em filtroAtual e textoBusca
    return this.tarefas; // SUBSTITUIR esta linha
  }

  // TODO 2: Implementar contador de pendentes
  get tarefasPendentes(): number {
    // IMPLEMENTAR: contar tarefas onde concluida = false
    return 0; // SUBSTITUIR esta linha
  }

  // TODO 3: Implementar método para adicionar tarefa
  adicionarTarefa(): void {
    if (this.tarefaForm.valid) {
      // IMPLEMENTAR:
      // 1. Pegar dados do formulário
      // 2. Criar nova tarefa com ID único
      // 3. Adicionar ao array de tarefas
      // 4. Resetar formulário
      
      console.log('Implementar adicionarTarefa()');
    }
  }

  // TODO 4: Implementar toggle de status
  toggleConcluida(id: number): void {
    // IMPLEMENTAR: encontrar tarefa por ID e inverter status concluida
    console.log('Implementar toggleConcluida() para ID:', id);
  }

  // TODO 5: Implementar remoção de tarefa
  removerTarefa(id: number): void {
    // IMPLEMENTAR: remover tarefa do array pelo ID
    console.log('Implementar removerTarefa() para ID:', id);
  }

  // TODO 6: Implementar mudança de filtro
  alterarFiltro(novoFiltro: string): void {
    // IMPLEMENTAR: alterar this.filtroAtual
    console.log('Implementar alterarFiltro() para:', novoFiltro);
  }

  // TODO 7: Implementar busca por texto
  buscarTarefas(evento: any): void {
    // IMPLEMENTAR: alterar this.textoBusca baseado no input
    console.log('Implementar buscarTarefas() com texto:', evento.target.value);
  }

  // Métodos auxiliares - JÁ IMPLEMENTADOS
  gerarProximoId(): number {
    return Math.max(...this.tarefas.map(t => t.id)) + 1;
  }

  formatarData(data: string): string {
    return new Date(data).toLocaleDateString('pt-BR');
  }

  isAtrasada(tarefa: Tarefa): boolean {
    return !tarefa.concluida && new Date(tarefa.dataLimite) < new Date();
  }
}
