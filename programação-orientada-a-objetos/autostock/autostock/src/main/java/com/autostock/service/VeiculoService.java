package com.autostock.service;

import java.math.BigDecimal;
import java.util.List;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import com.autostock.exception.RecursoNaoEncontradoException;
import com.autostock.exception.RegraNegocioException;
import com.autostock.model.Modelo;
import com.autostock.model.StatusVeiculo;
import com.autostock.model.Veiculo;
import com.autostock.repository.ModeloRepository;
import com.autostock.repository.VeiculoRepository;

@Service
public class VeiculoService {
    private final VeiculoRepository veiculoRepository;
    private final ModeloRepository modeloRepository;
    public VeiculoService(VeiculoRepository veiculoRepository, ModeloRepository modeloRepository) { this.veiculoRepository = veiculoRepository; this.modeloRepository = modeloRepository; }

    public List<Veiculo> listarTodos() { return veiculoRepository.filtrar(null, null, null, null, null, null); }
    public Veiculo buscarPorId(Long id) { return veiculoRepository.findById(id).orElseThrow(() -> new RecursoNaoEncontradoException("Veículo não encontrado.")); }

    @Transactional
    public Veiculo salvar(Veiculo veiculo) { veiculo.setModelo(resolverModelo(veiculo)); normalizar(veiculo); return veiculoRepository.save(veiculo); }
    @Transactional
    public Veiculo atualizar(Long id, Veiculo atual) {
        Veiculo v = buscarPorId(id); v.setModelo(resolverModelo(atual)); v.setAno(atual.getAno()); v.setCor(atual.getCor()); v.setPreco(atual.getPreco()); v.setQuilometragem(atual.getQuilometragem()); v.setStatus(atual.getStatus()); v.setObservacao(atual.getObservacao()); normalizar(v); return veiculoRepository.save(v);
    }
    @Transactional public void excluir(Long id) { veiculoRepository.delete(buscarPorId(id)); }

    public List<Veiculo> filtrar(Long marcaId, Long modeloId, StatusVeiculo status, Integer ano, BigDecimal precoMinimo, BigDecimal precoMaximo) {
        if (precoMinimo != null && precoMaximo != null && precoMinimo.compareTo(precoMaximo) > 0) throw new RegraNegocioException("O preço mínimo não pode ser maior que o preço máximo.");
        return veiculoRepository.filtrar(marcaId, modeloId, status, ano, precoMinimo, precoMaximo);
    }
    private Modelo resolverModelo(Veiculo v) {
        if (v.getModelo() == null || v.getModelo().getId() == null) throw new RegraNegocioException("Modelo é obrigatório.");
        return modeloRepository.findById(v.getModelo().getId()).orElseThrow(() -> new RecursoNaoEncontradoException("Modelo não encontrado."));
    }
    private void normalizar(Veiculo v) { if (v.getCor() != null) v.setCor(v.getCor().trim()); if (v.getObservacao() != null) v.setObservacao(v.getObservacao().trim()); }
}
