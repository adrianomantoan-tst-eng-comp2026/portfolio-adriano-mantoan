package com.autostock.repository;

import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;
import com.autostock.model.Marca;

public interface MarcaRepository extends JpaRepository<Marca, Long> {
    Optional<Marca> findByNomeIgnoreCase(String nome);
}
