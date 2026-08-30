package com.autostock.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import jakarta.persistence.UniqueConstraint;
import jakarta.validation.constraints.NotBlank;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "marcas", uniqueConstraints = @UniqueConstraint(name = "uk_marca_nome", columnNames = "nome"))
@Getter @Setter @NoArgsConstructor
public class Marca extends EntidadeBase {
    @NotBlank(message = "O nome da marca é obrigatório")
    @Column(nullable = false, length = 100)
    private String nome;
}
