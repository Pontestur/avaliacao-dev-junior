export interface Tarefa {
  id: number;
  titulo: string;
  descricao: string;
  concluida: boolean;
  prioridade: 'baixa' | 'media' | 'alta';
  dataLimite: string; // formato: 'YYYY-MM-DD'
  dataCriacao: string;
}
