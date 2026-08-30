package com.autostock.service;

import java.util.List;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import com.autostock.exception.RecursoNaoEncontradoException;
import com.autostock.exception.RegraNegocioException;
import com.autostock.model.Marca;
import com.autostock.model.Modelo;
import com.autostock.repository.MarcaRepository;
import com.autostock.repository.ModeloRepository;
import com.autostock.repository.VeiculoRepository;

@Service
public class ModeloService {
    private final ModeloRepository modeloRepository;
    private final MarcaRepository marcaRepository;
    private final VeiculoRepository veiculoRepository;

    public ModeloService(ModeloRepository modeloRepository, MarcaRepository marcaRepository, VeiculoRepository veiculoRepository) {
        this.modeloRepository = modeloRepository; this.marcaRepository = marcaRepository; this.veiculoRepository = veiculoRepository;
    }
    public List<Modelo> listarTodos() { return modeloRepository.findAll(); }
    public List<Modelo> listarPorMarca(Long marcaId) { buscarMarca(marcaId); return modeloRepository.findByMarcaIdOrderByNomeAsc(marcaId); }
    public Modelo buscarPorId(Long id) { return modeloRepository.findById(id).orElseThrow(() -> new RecursoNaoEncontradoException("Modelo não encontrado.")); }

    @Transactional
    public Modelo salvar(Modelo modelo) {
        Marca marca = resolverMarca(modelo);
        String nome = modelo.getNome().trim();
        modeloRepository.findByMarcaIdAndNomeIgnoreCase(marca.getId(), nome).ifPresent(m -> { throw new RegraNegocioException("Esse modelo já está cadastrado para a marca selecionada."); });
        modelo.setNome(nome); modelo.setMarca(marca); return modeloRepository.save(modelo);
    }
    @Transactional
    public Modelo atualizar(Long id, Modelo atual) {
        Modelo modelo = buscarPorId(id); Marca marca = resolverMarca(atual); String nome = atual.getNome().trim();
        modeloRepository.findByMarcaIdAndNomeIgnoreCase(marca.getId(), nome).filter(m -> !m.getId().equals(id)).ifPresent(m -> { throw new RegraNegocioException("Esse modelo já está cadastrado para a marca selecionada."); });
        modelo.setNome(nome); modelo.setMarca(marca); return modeloRepository.save(modelo);
    }
    @Transactional
    public void excluir(Long id) {
        buscarPorId(id);
        if (veiculoRepository.existsByModeloId(id)) throw new RegraNegocioException("Não é possível excluir o modelo porque existem veículos vinculados a ele.");
        modeloRepository.deleteById(id);
    }
    private Marca resolverMarca(Modelo modelo) {
        if (modelo.getMarca() == null || modelo.getMarca().getId() == null) throw new RegraNegocioException("Marca é obrigatória.");
        return buscarMarca(modelo.getMarca().getId());
    }
    private Marca buscarMarca(Long id) { return marcaRepository.findById(id).orElseThrow(() -> new RecursoNaoEncontradoException("Marca não encontrada.")); }
}
