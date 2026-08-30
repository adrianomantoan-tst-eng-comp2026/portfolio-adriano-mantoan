package com.autostock.service;

import java.util.List;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import com.autostock.exception.RecursoNaoEncontradoException;
import com.autostock.exception.RegraNegocioException;
import com.autostock.model.Marca;
import com.autostock.repository.MarcaRepository;
import com.autostock.repository.ModeloRepository;

@Service
public class MarcaService {
    private final MarcaRepository marcaRepository;
    private final ModeloRepository modeloRepository;

    public MarcaService(MarcaRepository marcaRepository, ModeloRepository modeloRepository) {
        this.marcaRepository = marcaRepository;
        this.modeloRepository = modeloRepository;
    }

    public List<Marca> listarTodas() { return marcaRepository.findAll(); }
    public Marca buscarPorId(Long id) { return marcaRepository.findById(id).orElseThrow(() -> new RecursoNaoEncontradoException("Marca não encontrada.")); }

    @Transactional
    public Marca salvar(Marca marca) {
        String nome = normalizar(marca.getNome());
        marcaRepository.findByNomeIgnoreCase(nome).ifPresent(m -> { throw new RegraNegocioException("Já existe uma marca com esse nome."); });
        marca.setNome(nome);
        return marcaRepository.save(marca);
    }

    @Transactional
    public Marca atualizar(Long id, Marca atualizada) {
        Marca marca = buscarPorId(id);
        String nome = normalizar(atualizada.getNome());
        marcaRepository.findByNomeIgnoreCase(nome).filter(m -> !m.getId().equals(id)).ifPresent(m -> { throw new RegraNegocioException("Já existe uma marca com esse nome."); });
        marca.setNome(nome);
        return marcaRepository.save(marca);
    }

    @Transactional
    public void excluir(Long id) {
        buscarPorId(id);
        if (modeloRepository.existsByMarcaId(id)) throw new RegraNegocioException("Não é possível excluir a marca porque existem modelos vinculados a ela.");
        marcaRepository.deleteById(id);
    }

    private String normalizar(String nome) { return nome == null ? null : nome.trim(); }
}
