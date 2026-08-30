package com.autostock.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import jakarta.persistence.UniqueConstraint;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "modelos", uniqueConstraints = @UniqueConstraint(name = "uk_modelo_marca_nome", columnNames = {"marca_id", "nome"}))
@Getter @Setter @NoArgsConstructor
public class Modelo extends EntidadeBase {
    @NotBlank(message = "O nome do modelo é obrigatório")
    @Column(nullable = false, length = 150)
    private String nome;

    @NotNull(message = "A marca é obrigatória")
    @ManyToOne(fetch = FetchType.EAGER, optional = false)
    @JoinColumn(name = "marca_id", nullable = false)
    private Marca marca;
}
