package com.autostock.repository;

import java.math.BigDecimal;
import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import com.autostock.model.StatusVeiculo;
import com.autostock.model.Veiculo;

public interface VeiculoRepository extends JpaRepository<Veiculo, Long> {
    boolean existsByModeloId(Long modeloId);

    @Query("""
        SELECT v FROM Veiculo v
        WHERE (:marcaId IS NULL OR v.modelo.marca.id = :marcaId)
          AND (:modeloId IS NULL OR v.modelo.id = :modeloId)
          AND (:status IS NULL OR v.status = :status)
          AND (:ano IS NULL OR v.ano = :ano)
          AND (:precoMinimo IS NULL OR v.preco >= :precoMinimo)
          AND (:precoMaximo IS NULL OR v.preco <= :precoMaximo)
        ORDER BY v.id DESC
        """)
    List<Veiculo> filtrar(
        @Param("marcaId") Long marcaId,
        @Param("modeloId") Long modeloId,
        @Param("status") StatusVeiculo status,
        @Param("ano") Integer ano,
        @Param("precoMinimo") BigDecimal precoMinimo,
        @Param("precoMaximo") BigDecimal precoMaximo
    );
}
