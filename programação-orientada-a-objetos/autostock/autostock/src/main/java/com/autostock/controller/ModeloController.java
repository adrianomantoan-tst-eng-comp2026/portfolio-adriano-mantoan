package com.autostock.controller;

import java.util.List;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.autostock.model.Modelo;
import com.autostock.service.ModeloService;
import jakarta.validation.Valid;

@RestController @RequestMapping("/api/modelos")
public class ModeloController {
    private final ModeloService service;
    public ModeloController(ModeloService service) { this.service = service; }
    @GetMapping public List<Modelo> listar(@RequestParam(required = false) Long marcaId) { return marcaId == null ? service.listarTodos() : service.listarPorMarca(marcaId); }
    @GetMapping("/{id}") public Modelo buscar(@PathVariable Long id) { return service.buscarPorId(id); }
    @PostMapping public ResponseEntity<Modelo> cadastrar(@Valid @RequestBody Modelo modelo) { return ResponseEntity.status(HttpStatus.CREATED).body(service.salvar(modelo)); }
    @PutMapping("/{id}") public Modelo atualizar(@PathVariable Long id, @Valid @RequestBody Modelo modelo) { return service.atualizar(id, modelo); }
    @DeleteMapping("/{id}") public ResponseEntity<Void> excluir(@PathVariable Long id) { service.excluir(id); return ResponseEntity.noContent().build(); }
}
