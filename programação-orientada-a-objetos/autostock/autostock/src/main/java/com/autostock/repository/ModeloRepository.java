package com.autostock.repository;

import java.util.List;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;
import com.autostock.model.Modelo;

public interface ModeloRepository extends JpaRepository<Modelo, Long> {
    List<Modelo> findByMarcaIdOrderByNomeAsc(Long marcaId);
    Optional<Modelo> findByMarcaIdAndNomeIgnoreCase(Long marcaId, String nome);
    boolean existsByMarcaId(Long marcaId);
}
